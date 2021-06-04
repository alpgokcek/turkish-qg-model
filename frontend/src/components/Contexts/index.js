import React, { useState } from "react";
import PropTypes from "prop-types";
import InputBox from "../InputBox";
import axios from "axios";
import "./contexts.scss";

const Contexts = (props) => {
  const { setQuestions } = props;
  const API_URL = "http://40.124.100.78:5000";

  const [state, setState] = useState([]);

  const handleAddInputBox = () =>
    setState([{ name: "", context: "", question: "", answer: "" }, ...state]);
  const handleAddTestDataInputBox = () => {
    axios
      .get(`${API_URL}/get-random-doc`)
      .then((resp) => resp.data)
      .then((data) => {
        const questions = data.data;
        const randQuestion = Math.floor(Math.random() * questions.length);
        setState([
          {
            name: data.name,
            context: data.description,
            question: questions[randQuestion].questions[0],
            answer: questions[randQuestion].answer,
          },
          ...state,
        ]);
      })
      .catch((err) => console.error(err));
    //const len = testData["data"].length
    //const randIdx = Math.floor(Math.random() * len);
    //const randDoc = testData["data"][randIdx]
    //console.log(randDoc)
  };
  const handleRemoveInputBox = (e, idx) => {
    const temp = [...state];
    temp.splice(idx, 1);
    setState([...temp]);
  };

  const handleChange = (e, idx) => {
    const tempArr = [...state];
    tempArr[idx] = { ...tempArr[idx], [e.target.name]: e.target.value };
    setState([...tempArr]);
  };

  const handleGenerateQuestions = () => {
    if (state.length === 0) return;
    axios
      .post(`${API_URL}/generate-questions`, {
        data: state.map((item) => ({
          description: item.context,
          data: [
            {
              questions: [item.question],
              answer: item.answer,
            },
          ],
        })),
      })
      .then((resp) => resp.data)
      .then((data) => setQuestions(data.data))
      .catch((err) => console.error(err));
  };
  return (
    <div className="contexts">
      <div className="contexts-button" onClick={handleAddInputBox}>
        + Add
      </div>
      <div className="contexts-button" onClick={handleAddTestDataInputBox}>
        + Add Test Data
      </div>
      <div>Document Count: {state.length}</div>
      {state.map((box, idx) => (
        <InputBox
          key={idx}
          id={idx}
          data={box}
          onChange={handleChange}
          onRemove={handleRemoveInputBox}
        />
      ))}
      {state.length > 0 && (
        <div className="contexts-button" onClick={handleGenerateQuestions}>
          Generate Questions
        </div>
      )}
    </div>
  );
};

Contexts.propTypes = {
  questions: PropTypes.array,
  setQuestions: PropTypes.func,
};

export default Contexts;
