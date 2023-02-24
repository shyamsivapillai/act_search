import { ArrowRight, ArrowLeft } from 'react-bootstrap-icons';

function Paginator(props) {

    const renderPaginatorTitle = () => {
        const pageMeta = props.pageMeta
        const initialLoad = props.initialLoad;
        const {total_results: totalResults} = pageMeta[0]
        return !initialLoad ? <h4>Found {totalResults} results</h4> : <></>


    }

    const renderPaginatorBar = () => {
        const pageMeta = props.pageMeta
        const pageNumber = props.pageNumber;
        const {total_pages: totalPages} = pageMeta[0];
        if (totalPages) {
            return (
                <>
                    <span>
                        <ArrowLeft onClick={() => props.togglePaginate("backward")} />
                            Showing {pageNumber} of {totalPages ? totalPages : 0}
                        <ArrowRight onClick={() => props.togglePaginate("forward")} />
                    </span>
                </>
            )
        } else {
            return <></>
        }
        
    }

    return (
        <>
            {renderPaginatorTitle()}
            {renderPaginatorBar()}
        </>
    )
}

export default Paginator