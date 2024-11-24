import React from "react";
import "../assets/css/about.css"; 

export default function AboutPage() {
  return (
    <div className="about-page">
      <div className="content">
        <img
          src="https://i.imgur.com/5fd3g8j.png"
          alt="CramDam Logo"
          className="logo"
        />
        <h1 className="title">About CramDam</h1>
        <p className="subtext">
          Built by Beavers, for Beavers. CramDam is your ultimate companion for
          collaborative learning and academic success. Built to connect students
          with study buddies, upcoming study sessions, and personalized
          resources, CramDam turns studying into a fun and engaging experience.
          Whether you're looking to prepare for exams, work on group projects,
          or just enhance your understanding of a subject, our platform makes it
          easy to find like-minded peers who share your goals and learning
          style.
        </p>
        <p className="subtext">
          Collaboration isn't just beneficial; it's essential for growth. By
          teaming up with others, you can explore new perspectives, break down
          challenging topics, and stay motivated on your academic journey.
          CramDam is designed to foster meaningful connections in a dynamic,
          interactive environment that makes learning enjoyable. With tools like
          a personalized dashboard, course hubs, and fun gamification features,
          CramDam helps you turn studying into something you’ll look forward to
          every day!
        </p>
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
