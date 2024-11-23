import React from "react";
import "../assets/css/login.css";

export default function LoginPage() {
  return (
    <div className="login-page">
      <div className="form-container">
        <h1>Login</h1>
        <form>
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

          {/* Submit Button */}
          <button type="submit" className="btn submit">
            Login
          </button>
        </form>
      </div>
    </div>
  );
}
