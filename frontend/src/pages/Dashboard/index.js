import React, {useState} from 'react';
import Contexts from '../../components/Contexts';
import Questions from '../../components/Questions';

import "./dashboard.scss";

const Dashboard = () => {
  const [questions, setQuestions] = useState([])


  return (
    <div>
      <div className="dashboard-wrapper">
        <Contexts questions={questions} setQuestions={setQuestions}/>
        <Questions questions={questions}/>
      </div>
    </div>
  );
};

Dashboard.propTypes = {};

export default Dashboard;
