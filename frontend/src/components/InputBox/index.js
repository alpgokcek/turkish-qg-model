import React from "react";
import PropTypes from "prop-types";

import "./input-box.scss";

const InputBox = (props) => {
  const { id, data:{context, answer, name, question}, onChange, onRemove } = props;
  return (
    <div className="input-box">
      <div className="input-box-title">{`Document ${id + 1}:`}</div>

      <div className="input-box__wrapper">
        <div className="input-box__wrapper-inputs">
          <input className="input-box-input" value={name}
            onChange={(e) => onChange(e, id)} name="name" placeholder="Name" />

          <input className="input-box-input" value={question}
            onChange={(e) => onChange(e, id)} name="question" placeholder="Question" />
          
          <input className="input-box-input" value={answer}
            onChange={(e) => onChange(e, id)} name="answer" placeholder="Answer" />
          
          <textarea
            name="context"
            className="input-box-text-area"
            placeholder="Context"
            value={context}
            onChange={(e) => onChange(e, id)}
          />
        </div>

        <span className="input-box-remove" onClick={(e) => onRemove(e, id)}>
          <img src="images/delete.png" alt="delete" />
        </span>
      </div>
    </div>
  );
};

InputBox.propTypes = {
  id: PropTypes.number,
  data: PropTypes.string,
  onChange: PropTypes.func,
  onRemove: PropTypes.func,
};

export default InputBox;
