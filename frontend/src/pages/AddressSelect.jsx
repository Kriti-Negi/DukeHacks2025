import Navbar from "../components/Navbar";
import "../styles/general.css";

export default function AddressSelect(){


    function nextPage(){

    }

    return (
        <div>
            <Navbar pageName = "Find Your House"/>

            <div>
                <input
                    className = "input-set"
                    placeholder = "Enter Address"
                />
                <button className = "btn">Search</button>
            </div>

            <iframe
                width="100%"
                height="425"
                loading="lazy"
                allowfullscreen
                referrerpolicy="no-referrer-when-downgrade"
                src="https://www.google.com/maps/embed/v1/place?key=lol
                    &q=Space+Needle,Seattle+WA">
            </iframe>

            <button className = "btn btn-next">Next</button>
            
        </div>

    )
}