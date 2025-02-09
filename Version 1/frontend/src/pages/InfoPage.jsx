import Card from "../components/Card";
import Navbar from "../components/Navbar";
import "../styles/infoPageStyles.css";
import leaf from "../images/leaf.png"
import Chart from "../components/Chart";
import { useLocation } from "react-router";

import { useEffect, useState } from "react";

export default function InfoPage(props){

    const { state: { infoId } = {} } = useLocation();
    const { state: { numberOfFloors } = {} } = useLocation();
    const { state: { roofType } = {} } = useLocation();

    const [bill, setBill] = useState(300);
    const [month, setMonth] = useState(0);
    const [solarPanelType, setSolarPanelType] = useState(1);

    const [numSolarPanels, setNumSolar] = useState(0);

    const [hasEstimate, setHasEstimate] = useState(false);
    const [dataObtained, setDataObtained] = useState({});

    const [img, setImg] = useState();

    async function getEstimate(){
        
        if(bill && month && solarPanelType != -1){
            console.log(roofType);

                    let address = "address=" + infoId;
                    let material = "material=" + roofType;
                    let elecBill = "bill=" + bill;
                    let elecMonth = "monthID=" + month;
                    let roofLevel = "roofLevel=" + numberOfFloors;
                    let ELECTRICITY_RATE;

                    if(solarPanelType == 0){
                        ELECTRICITY_RATE = "solarCost=" +  "" + 0.163;
                    }
                    
                    const response = await fetch('http://127.0.0.1:5000/getEstimate?' + 
                            address + "&" + material + "&" + elecBill + "&" + elecMonth + "&" + ELECTRICITY_RATE + "&" + roofLevel
                    );

                    console.log(response);

                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }

                    const json = await response.json();

                    setDataObtained(json);

                    setHasEstimate(true);
                    setImg();
                    getImage();
        }
    }

    async function getImage(){
        if(!img && bill && month && solarPanelType != -1){
            let address = "address=" + infoId;

            const response = await fetch(
                'http://127.0.0.1:5000/giveImage?' + address, 
                {
                    headers: {
                        'Content-Type': 'image/png'
                    }
                });

            console.log(response);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json()
            setImg(data.url);
        }
    }

    function getHighDetailText(){
        if(hasEstimate){
            return "Some text"
        }else{
            return ""
        }
    }

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
                            src={"https://www.google.com/maps/embed/v1/place?key=key&zoom=33&q=" + infoId}>
                        </iframe>
                    </div>

                    {hasEstimate && <h3>CARBON FOOTPRINT</h3>}

                    {hasEstimate && <div className="eco-facts"> <div className="eco-fact"> <img src = {leaf}/> <p>You carbon emissions are cut by {Math.floor(dataObtained.carbonFootprintOffset)} lbs/building per year</p> </div></div>} 

                    {hasEstimate && <h3>SOLAR MAP</h3>}
                    {hasEstimate && <p>Lighters areas are better for adding solar panels</p>}

                    <div>
                        {hasEstimate && <img className = "solarMapStyles" src = {"http://127.0.0.1:5000/giveImage?address=" + infoId}/>}
                    </div>

                </div>
                <div className = "right">

                <h3>Solar Panels</h3>
                    <div className = "cards">
                        <Card
                            compName="REC Group"
                            cost="0.16 kW/hr"
                            modelnum="Model: Alpha Pura 410W."
                            id = {0}
                            isSelected = {solarPanelType}
                            setSelected = {setSolarPanelType}
                        />
                    </div>

                    <input 
                        placeholder = "Enter Monthly Electricity Bill"
                        onChange={(e) => setBill(e.target.value)}
                        type = "number"
                    ></input>

                    <div className="dropdown">
                        <label for="months">Select a Month:</label>
                        <select id="months" name="Months" onChange={(e) => setMonth(e.target.value)}>
                            <option value="0">January</option>
                            <option value="1">February</option>
                            <option value="2">March</option>
                            <option value="3">April</option>
                            <option value="4">May</option>
                            <option value="5">June</option>
                            <option value="6">July</option>
                            <option value="7">August</option>
                            <option value="8">September</option>
                            <option value="9">October</option>
                            <option value="10">November</option>
                            <option value="11">December</option>
                        </select>
                    </div>
                    
                    <button 
                        className="btn-calc"
                        onClick={() => {getEstimate()}}
                    >Calculate</button>

                    {hasEstimate && <div><h3>STATS AND INFO</h3> <Chart a = {dataObtained.totalYearlyCost} b = {dataObtained.yearlySavings}/> </div>}

                    {hasEstimate && <h3>MONEY SAVED</h3>}
                    {hasEstimate && <p style={{height: "20px"}}>  </p>}

                    {hasEstimate && <p>Total Yearly Cost: ${Math.floor(dataObtained.totalYearlyCost)}</p>}
                    {hasEstimate && <p>Total Installation Cost: ${dataObtained.totalInstallationCost}</p>}
                    {hasEstimate && <p>Ideal Number of Solar Panels: {dataObtained.numPanels}</p>}
                    {hasEstimate && <p>NPV in 25 Years: {Math.floor(dataObtained.npv)}</p>}
                    {hasEstimate && <p>ROI: {Math.round(dataObtained.ROI, 2)} %</p>}
                    {hasEstimate && <p>Area: {Math.round(dataObtained.area)} m^2</p>}
                    {hasEstimate && <p style={{height: "30px"}}>  </p>}

                </div>
            </main>

        </div>
    )
}

/*

 "totalYearlyCost": total_yearly_cost,

        "totalInstallationCost": total_installation_cost,
        "yearlySavings": yearly_savings,
        "numPanels": num_panels,
        "npv": npv_25_years,
        "paybackPeriod": payback_period,
        "ROI": (ROI * 100)*/


        /*

        <label for="numSolar">Number of Solar Panels: {numSolarPanels} </label> <br/>
                    <input className="slider" style = {{width: "100%"}} type="range" id="numSolar" name="solar" min="0" max="100" step="1" onChange={(e) => setNumSolar(e.target.value)}/>*/
