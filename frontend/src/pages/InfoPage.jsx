import Card from "../components/Card";
import Navbar from "../components/Navbar";
import "../styles/infoPageStyles.css";
import leaf from "../images/leaf.png"
import Chart from "../components/Chart";
//AIzaSyAnPDXizb6BbI0QORyg8pUk9mXkPasTzZI

export default function InfoPage(){
    return (
        <div>
            <Navbar pageName = "Summary"/>
            <main>
                <div className = "left">
                    <div className="map-container">
                        <iframe
                            width="100%"
                            height="250"
                            loading="lazy"
                            allowfullscreen
                            referrerpolicy="no-referrer-when-downgrade"
                            src="https://www.google.com/maps/embed/v1/place?key=//
                                &q=Space+Needle,Seattle+WA">
                        </iframe>
                    </div>
                    <h3>Solar Panels</h3>
                    <scroll>
                        <div className = "cards">
                        <Card
                            compName="dkslfjskdf"
                            cost="sdfsd"
                            otherInfo="dsfsdf"
                        />
                        </div>
                    </scroll>
                </div>
                <div className = "right">
                    <h3>MONEY SAVED</h3>

                    <input placeholder = "Enter Monthly Electricity Bill"></input>
                    <button className="btn-calc">Calculate</button>

                    <h3>STATS AND INFO</h3>

                    <Chart/>

                    <h3>CARBON FOOTPRINT</h3>

                    <div className="eco-facts">
                        <div className="eco-fact">
                            <img src = {leaf}/>
                            <p>FUN FACTS ABOUT HOW IT REDUCES CARBON FOOTPRINT AND IS GREAT FOR THE ENVIORNMENT</p>
                        </div>
                    </div>

                </div>
            </main>
            

        </div>
    )
}