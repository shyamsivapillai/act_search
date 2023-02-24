import time
from flask import Flask, request
from flask_cors import CORS
from sqlalchemy.engine import create_engine
from sqlalchemy.sql import text
from .settings import get_settings
from .db.initialize import initialize_data
import math

app = Flask(__name__)
CORS(app)

initialize_data()

settings = get_settings()

DB_URI = settings["DB_URI"]
RESULT_PAGE_LIMIT = settings["RESULT_PAGE_LIMIT"]

@app.route('/health')
def get_health():
    return {'msg': 200}

@app.route('/search', methods=['POST'])
def get_search():
    
    query = request.args.get("q")
    page_number = int(request.args.get("page", 1))
    page_number = page_number - 1
    offset = RESULT_PAGE_LIMIT * page_number

    engine = create_engine(DB_URI, echo=True)
    results = engine.execute(
        text(
            f'''
                SELECT s.section_text, s.est_section_num, a.id, a.name 
                FROM sections AS s
                INNER JOIN acts AS a on s.act_id = a.id WHERE section_text
                LIKE '%{query}%' ORDER BY a.name LIMIT 10 OFFSET {offset}
            '''
            )
        )
    
    total_result_counts = engine.execute(
        text(
            f'''
                SELECT COUNT(*) FROM sections AS s
                INNER JOIN acts AS a on s.act_id = a.id WHERE section_text
                LIKE '%{query}%'
            '''
            )
        ).scalar()

    data = []
    for row in results:
        curr_row = {}
        curr_row["section_text"] = row[0]
        curr_row["est_section_num"] = row[1]
        curr_row["act_id"] = row[2]
        curr_row["act"] = row[3]
        data.append(curr_row)
    
    page_meta = {
        "total_pages": math.ceil(total_result_counts/RESULT_PAGE_LIMIT),
        "page_number": max(page_number, 1),
        "page_size": RESULT_PAGE_LIMIT,
        "page_result_count": results.rowcount,
        "total_results": total_result_counts
    },

    return {"results": data, "page_meta": page_meta}