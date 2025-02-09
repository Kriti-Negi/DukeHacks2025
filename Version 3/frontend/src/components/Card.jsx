import "../styles/cards.css";

export default function Card(props){

    function dealWithClick(){
        props.setSelected(props.id);
    }

    return (
        <div className = "card">
            <div className="card-heading">
                <h3>{props.compName}</h3>
                <p>COST: {props.cost}</p>
            </div>
            <p className="more-info">{props.otherInfo}</p>

            {props.id == props.isSelected && <button style= {{backgroundColor: "#64FF58"}} className="btn btn-select" onClick={() => dealWithClick()}>SELECT</button>}
            {props.id !== props.isSelected && <button className="btn btn-select" onClick={() => dealWithClick()}>SELECT</button>}
        </div>
    )
}