import React from "react";
import { Router, Switch, Route, Redirect } from "react-router-dom";
import { createBrowserHistory } from "history";
import Layout from "./components/Layout";
import Dashboard from "./pages/Dashboard";

function RouteWrapper({ component: Component, ...rest }) {
  return (
    <Route
      {...rest}
      render={(props) => (
        <Layout>
          <Component {...props} />
        </Layout>
      )}
    />
  );
}

const browserHistory = createBrowserHistory();

const App = () => {
  return (
    <Router history={browserHistory}>
      <Switch>
        <RouteWrapper
          path="/"
          component={Dashboard}
        />
        <Redirect to="/"/>
      </Switch>
    </Router>
  );
};

App.propTypes = {};

export default App;
