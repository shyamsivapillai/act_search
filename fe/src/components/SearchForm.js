import  { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import ResultsTable from './ResultsTable';
import Paginator from './Paginator';

function BasicExample() {

    const [search, setSearch] = useState('');
    const [results, setResults] = useState({results: [{}], page_meta: [{}], initial_load: true})
    const [pageNumber, setPageNumber] = useState(1)

    const searchSections = () => {
        
        fetch(`http://localhost:5000/search?q=${search}&page=${pageNumber}`, {method: 'POST'}).then(res => res.json()).then(data => {
            data["initial_load"] = false
            setResults(data)
            setPageNumber(1)
        });
    }

    const togglePagination = (direction) => {
        if (direction === "forward" && pageNumber < results["page_meta"][0]["total_pages"]) {
            console.log("here tooo")
            setPageNumber(pageNumber + 1)
            fetch(`http://localhost:5000/search?q=${search}&page=${pageNumber + 1}`, {method: 'POST'}).then(res => res.json()).then(data => {
                data["initial_load"] = false
                setResults(data)
            });
        } else if (direction == "backward" && pageNumber > 1 ) {
            setPageNumber(pageNumber - 1)
            fetch(`http://localhost:5000/search?q=${search}&page=${pageNumber - 1}`, {method: 'POST'}).then(res => res.json()).then(data => {
                data["initial_load"] = false
                setResults(data)
            });
        }
    }

    return (
        <Container>
            <Row className="justify-content-md-center">
                {/* <Col xs lg="4">
                1 of 3
                </Col> */}
                <Col md="auto">
                    <Form.Control type="text" onChange={(e) => setSearch(e.target.value)} placeholder="Enter search term" />
                </Col>
                <Col xs lg="2">
                    <Button onClick={searchSections} variant="primary" type="submit">
                        Submit
                    </Button>
                </Col>
            </Row>

        <hr/>

        <Row className="justify-content-md-center">
            <Paginator
                pageMeta={results.page_meta}
                pageNumber={pageNumber}
                initialLoad={results.initial_load}
                togglePaginate={togglePagination}
            />
        </Row>

        <Row className="justify-content-md-center">
            <ResultsTable pageMeta={results} />
        </Row>
        </Container>
    );
}

export default BasicExample;