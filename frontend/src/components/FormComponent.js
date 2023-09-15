const FormComponent = ({ setCountry, setSeason, handleSubmit, season }) => {
  return (
    <>
      <div className="form">
        <div>
          <label>Enter a Country: </label>
          <input type="text" onChange={(e) => setCountry(e.target.value)} />
        </div>
        <div>
          <label>Select a Season: </label>
          <select
            name="seasons"
            id="seasons"
            value={season}
            onChange={(e) => setSeason(e.target.value)}
          >
            <option value="Summer">Summer</option>
            <option value="Winter">Winter</option>
            <option value="Autumn">Autumn</option>
            <option value="Spring">Spring</option>
          </select>
        </div>
      </div>
      <button className="submit-button" onClick={handleSubmit}>
        Get Recommendations
      </button>
    </>
  );
};

export default FormComponent;
