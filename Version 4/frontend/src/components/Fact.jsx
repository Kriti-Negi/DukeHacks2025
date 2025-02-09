export default function Fact(props){
    return (
        <div className="fact-card">
            <p>{props.info}</p>
            <h2>{props.num}</h2>
        </div>
    )
}