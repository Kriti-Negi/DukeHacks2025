import "../styles/general.css"

export default function Navbar(props){
    return (
        <div className="navbar">
            <h3>{props.pageName}</h3>
        </div>
    )
}