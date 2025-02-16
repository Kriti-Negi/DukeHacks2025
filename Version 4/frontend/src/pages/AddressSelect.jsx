import { use, useState } from "react";
import Navbar from "../components/Navbar";
import "../styles/general.css";
import { Link } from "react-router";

export default function AddressSelect(props){



    const [setAdd, setSetAdd] = useState("UNC Chapel Hill");
    const [address, setAddress] = useState("");

    const [roofType, setRoofType] = useState("other");
    const [numberOfFloors, setNumberOfFloors] = useState(0);

    return (
        <div>
            <Navbar pageName = "Find Your House"/>

            <div className="form">
                <input
                    className = "input-set"
                    placeholder = "Enter Address"
                    value={address}
                    onChange={
                        (e) => {
                            setAddress(e.target.value);
                            props.setAdd(e);
                        }
                    }
                />

                <div className="dropdown">
                    <label for="months">Select a Roof Type:</label>
                    <select id="months" name="Months" onChange={(e) => setRoofType(e.target.value)}>
                        <option value="metal">metal</option>
                        <option value="shingles">shingles</option>
                        <option value="concrete">concrete</option>
                        <option value="clay">clay</option>
                        <option value="other">other</option>
                    </select>
                </div>

                <input onChange = {(e) => setNumberOfFloors(e.target.value)} type = "number" className = "input-set" placeholder="Number Of Floors"></input> <br/>

                <button className = "btn" onClick={(e) => {setSetAdd(address); props.setAdd(address);}}>Search</button>
                
            </div>

            <iframe
                width="100%"
                height="425"
                loading="lazy"
                zoom="3"
                allowfullscreen
                referrerpolicy="no-referrer-when-downgrade"
                src={"https://www.google.com/maps/embed/v1/place?key=AIzaSyCLHNFewVkVLoUAG6eFTpgUmv_s9_vvgb4&zoom=33&q=" + setAdd}>
            </iframe>

            <Link
                to= "/infopage"
                state={
                    {infoId: setAdd, numberOfFloors: numberOfFloors, roofType: roofType}
                }
            >
                <a href = "/infopage">
                    <button onClick = {props.setAdd(setAdd)} className = "btn btn-next">Next</button>
                </a>
            </Link>            
            
        </div>

    )
}
