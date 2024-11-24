import React from "react";
import { Link } from "react-router-dom";
import "../assets/css/navbar.css";

export default function Navbar() {
  return (
    <div className="navbar">
      <ul>
        {/* Tabs */}
        <li className="tab">
          <Link to="/dashboard">My Profile</Link>
        </li>
        <li className="tab">
          <Link to="/coursehub">CourseHub</Link>
        </li>
        <li className="tab">
          <Link to="/studybuddyfinder">Study Buddy Finder</Link>
        </li>
      </ul>

      {/* Logout Button */}
      <button className="logout-btn" onClick={() => alert("Logged out!")}>
        Logout
      </button>
    </div>
  );
}
