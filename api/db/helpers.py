from .schemas import Acts, Sections

def write_act(act_data: dict, act_blob: str, session):
    bulk_objs = []
    name = act_data["name"]
    del act_data["name"]

    act = Acts(
            name=name,
            blob=act_blob
        )

    session.add(act)
    session.flush()

    bulk_objs.append(act)

    for k,v in act_data.items():
        bulk_objs.append(
            Sections(
                est_section_num=k,
                section_text=v,
                act_id=act.id
            )
        )
    
    return bulk_objs