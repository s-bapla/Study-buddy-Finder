import React, { useState } from "react";
import Navbar from "../components/Navbar";
import "../assets/css/dashboard.css";

export default function Dashboard() {
  const [profilePicture, setProfilePicture] = useState(null);

  // Handle profile picture upload
  const handleProfilePictureChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = () => {
        setProfilePicture(reader.result); // Set the uploaded image preview
      };
      reader.readAsDataURL(file);
    }
  };

  return (
    <div className="dashboard">
      {/* Navbar */}
      <Navbar />

      {/* Profile Summary */}
      <div className="profile-summary">
        <div className="profile-summary-header">
          <h1>Profile Summary</h1>
          <div className="profile-summary-actions">
            <button className="btn save">Save</button>
            <button className="btn edit">Edit</button>
          </div>
        </div>
        <form className="profile-form">
          {/* Profile Header: Profile Picture and Fields */}
          <div className="row profile-header">
            {/* Profile Picture */}
            <div className="profile-picture-container">
              <label
                htmlFor="profile-picture-upload"
                className="profile-picture"
                style={{
                  backgroundImage: profilePicture
                    ? `url(${profilePicture})`
                    : "none",
                }}
              >
                {!profilePicture && "Click to upload"}
              </label>
              <input
                type="file"
                id="profile-picture-upload"
                className="hidden-input"
                accept="image/*"
                onChange={handleProfilePictureChange}
              />
            </div>

            {/* Fields for Name, Major, and Year */}
            <div className="profile-fields">
              <div className="form-group">
                <label htmlFor="name">Name:</label>
                <input type="text" id="name" placeholder="Enter your name" />
              </div>
              <div className="form-group">
                <label htmlFor="major">Major:</label>
                <input type="text" id="major" placeholder="Enter your major" />
              </div>
              <div className="form-group">
                <label htmlFor="year">Year:</label>
                <select id="year">
                  <option value="freshman">Freshman</option>
                  <option value="sophomore">Sophomore</option>
                  <option value="junior">Junior</option>
                  <option value="senior">Senior</option>
                  <option value="graduate">Graduate</option>
                </select>
              </div>
            </div>
          </div>

          {/* Second Row: Autobiography */}
          <div className="profile-autobiography">
            <div className="form-group autobiography-container">
              <label htmlFor="autobiography" className="autobiography-label">
                Autobiography:
              </label>
              <textarea
                id="autobiography"
                className="autobiography-text"
                rows="6"
                placeholder="Write about yourself..."
              ></textarea>
            </div>
          </div>

          {/* Other Fields in Two Columns */}
          <div className="columns">
            {/* Left Column */}
            <div className="column">
              {/* Availability */}
              <div className="form-group">
                <label>Availability:</label>
                <div className="availability-options">
                  <label>
                    <input type="checkbox" value="morning" /> Morning
                  </label>
                  <label>
                    <input type="checkbox" value="afternoon" /> Afternoon
                  </label>
                  <label>
                    <input type="checkbox" value="evening" /> Evening
                  </label>
                  <label>
                    <input type="checkbox" value="night" /> Night
                  </label>
                </div>
              </div>

              {/* Remote/In-person */}
              <div className="form-group">
                <label>Remote or In-Person:</label>
                <select id="remote-or-in-person">
                  <option value="remote">Remote</option>
                  <option value="in-person">In-Person</option>
                  <option value="both">Both</option>
                </select>
              </div>
            </div>

            {/* Right Column */}
            <div className="column">
              {/* Study Type */}
              <div className="form-group">
                <label>Study Type:</label>
                <select id="study-type">
                  <option value="casual">Casual</option>
                  <option value="balanced">Balanced</option>
                  <option value="focused">Focused</option>
                </select>
              </div>
              {/* Learning Style */}
              <div className="form-group">
                <label>How You Learn Best:</label>
                <select id="learning-style">
                  <option value="visual">Visual</option>
                  <option value="auditory">Auditory</option>
                  <option value="experimental">Experimental</option>
                  <option value="combination">Combination</option>
                </select>
              </div>
            </div>
          </div>

          {/* Free-Response Fields */}
          <div className="free-response">
            {/* Enrolled Courses */}
            <div className="form-group">
              <label>Currently Enrolled Courses:</label>
              <input type="text" id="courses" placeholder="List your courses" />
            </div>

            {/* Upcoming Study Sessions */}
            <div className="form-group">
              <label>Upcoming Study Sessions:</label>
              <textarea
                id="study-sessions"
                rows="3"
                placeholder="Add your upcoming sessions"
              ></textarea>
            </div>

            {/* Current Study Buddy Matches */}
            <div className="form-group">
              <label>Current Study Buddy Matches:</label>
              <textarea
                id="study-buddies"
                rows="3"
                placeholder="List your matches"
              ></textarea>
            </div>

            {/* Student Calendar */}
            <div className="form-group">
              <label>Student Calendar:</label>
              <input type="file" id="calendar" accept=".ics" />
            </div>
          </div>
        </form>
      </div>
    </div>
  );
}
