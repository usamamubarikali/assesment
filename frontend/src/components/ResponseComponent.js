
const ResponseComponent = ({recommendations}) => {
    return (
      <>
        <h3>
            Our recommendations:
        </h3>
        {recommendations?.map((recommendation)=>(
            <p>{recommendation}</p>
        ))}

      </>
    );
  };
  
  export default ResponseComponent;
  