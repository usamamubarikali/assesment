import React, { useEffect, useState } from "react";
import axios from "axios";
import ResponseComponent from "../components/ResponseComponent";
import FormComponent from "../components/FormComponent";

const MainPage = () => {
  const [country, setCountry] = useState("");
  const [season, setSeason] = useState("Winter");
  const [recommendations, setRecommendations] = useState([]);

  const handleSubmit = async (e) => {
    try{
      const response = await axios.get(
          `http://localhost:3000/recommendations?country=${country}&season=${season}`
        )
      setRecommendations(response.data.recommendations)
    } catch (e) {
      console.log(e);
    }
      
  }

  return (
    <div className="main-div">
      <h1>Let me recommend you some good places :)</h1>
      <FormComponent
        setCountry={setCountry}
        setSeason={setSeason}
        handleSubmit={handleSubmit}
        season={season}
      />
      {recommendations.length ? <ResponseComponent recommendations={recommendations} /> : null}
    </div>
  );
};

export default MainPage;
