import React from "react";
import "../assets/css/landing.css"; // Include CSS for LandingPage

export default function LandingPage() {
  return (
    <div className="landing-page">
      <div className="content">
        <img
          src="https://i.imgur.com/LYhoZSp.png"
          alt="CramDam Logo"
          className="logo"
        />
        <h1 className="title">CramDam</h1>
        <p className="subtext">Welcome to the fam</p>
        <div className="button-group">
          <button
            onClick={() => (window.location.href = "/login")}
            className="btn login"
          >
            Login
          </button>
          <button
            onClick={() => (window.location.href = "/register")}
            className="btn register"
          >
            Register
          </button>
        </div>
      </div>
    </div>
  );
}
