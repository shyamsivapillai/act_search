function HighlightedText(props) {
    const text = props.text;
    const highlight = props.highlight;
    const textArr = props.text.split(" ")
    for (let i = 0; i < text.length; i++) {
        let curr = textArr[i]
        if (curr && curr.includes(highlight)) {
            curr = <span key={i} style={{"backgroundColor": "yellow"}}>{curr} </span>
        } else {
            curr = <span key={i}>{textArr[i]} </span>
        }
        textArr[i] = curr;
    }

    return <span>{textArr.map(x => x)}</span>
}

export default HighlightedText;