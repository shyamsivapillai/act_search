import Table from 'react-bootstrap/Table';
import HighlightedText from './HighlightedText';
function ResultsTable(props) {

  const renderData = () => {
    const pageMeta = props.pageMeta;
    const searchTerm = props.searchTerm;
    if (pageMeta["initial_load"] == true) {
        return <></>
    } else {
        const {results} = pageMeta;
        return (<tbody>
            {results.map((x, idx) => (
            <tr key={idx}>
                <td>{idx}</td>
                <td>{x["act"]}</td>
                <td>{x["est_section_num"]}</td>
                <td><HighlightedText highlight={searchTerm} text={x["section_text"]}/></td>
            </tr>
            ))}
            </tbody>)
    }
  }

  const renderTable = () => {
    const pageMeta = props.pageMeta;
    if (pageMeta["initial_load"]) {
        return <h3>Search through sections in Indian Laws</h3>
    } else {
        return (
            <Table striped bordered hover size="sm">
                <thead>
                    <tr>
                    <th>#</th>
                    <th>Act Name</th>
                    <th>Section ( Est. )</th>
                    <th>Section Text</th>
                    </tr>
                </thead>
                {renderData()}
            </Table>
        )
    }
  }

  return (
    <>
        {renderTable()}
    </>
  );
}

export default ResultsTable;