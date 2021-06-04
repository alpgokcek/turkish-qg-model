import React from "react";
import "./header.scss";

const Header = () => {
  return (
    <div className="header">
      <div className="header__wrapper">
      <img
        alt="hepsiburada logo"
        src="images/logo.png"
        className="header__logo"
      />
      </div>
    </div>
  );
};

export default Header;
