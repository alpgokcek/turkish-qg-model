import React from "react";
import PropTypes from "prop-types";

import "./questions.scss";

const Questions = (props) => {
  const { questions } = props;
  return (
    <div className="questions">
      <div className="questions-title">Generated Questions</div>
      <br />
      <ul className="questions__wrapper">
        {questions?.map((item, idx) => {
          return (
            <div key={idx} className="questions__container">
              <li className="questions-item"><b>Ground Truth: </b>{item[0].replace(" '", "'")}</li>
              <li className="questions-item"><b>Prediction: </b>{item[1].replace(" '", "'")}</li>
              <hr/>
            </div>
          );
        })}
      </ul>
    </div>
  );
};

Questions.propTypes = {
  questions: PropTypes.array,
};

export default Questions;
