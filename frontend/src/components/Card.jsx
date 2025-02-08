import "../styles/cards.css";

export default function Card(props){
    return (
        <div className = "card">
            <div className="card-heading">
                <h3>{props.compName}</h3>
                <p>COST: {props.cost}</p>
            </div>
            <p className="more-info">{props.otherInfo}</p>
            
            <button className="btn btn-select">SELECT</button>
        </div>
    )
}