import React from "react";
import "../assets/css/registration.css";

export default function Registerpage() {
  return (
    <div className="registration-page">
      <div className="form-container">
        <h1>Register</h1>
        <form>
          {/* Name Field */}
          <div className="form-group">
            <label htmlFor="name">Name</label>
            <input
              type="text"
              id="name"
              placeholder="Enter your name"
              required
            />
          </div>

          {/* Email Field */}
          <div className="form-group">
            <label htmlFor="email">Email</label>
            <input
              type="email"
              id="email"
              placeholder="Enter your email"
              required
            />
          </div>

          {/* Password Field */}
          <div className="form-group">
            <label htmlFor="password">Password</label>
            <input
              type="password"
              id="password"
              placeholder="Enter your password"
              required
            />
          </div>

          {/* Confirm Password Field */}
          <div className="form-group">
            <label htmlFor="confirm-password">Confirm Password</label>
            <input
              type="password"
              id="confirm-password"
              placeholder="Re-enter your password"
              required
            />
          </div>

          {/* Submit Button */}
          <button type="submit" className="btn submit">
            Register
          </button>
        </form>
      </div>
    </div>
  );
}
