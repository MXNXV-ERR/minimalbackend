import { useState, useRef } from "react";
import React from 'react';
import './DropBox.css'
import axios from "axios";

function DropBox() {
  const [image, setImage] = useState(null);
  const fileInputRef = useRef();

  function handleDrop(event) {
    event.preventDefault();
    const file = event.dataTransfer.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function() {
      setImage(reader.result);
    }
  }

  function handleDragOver(event) {
    event.preventDefault();
  }

  function handleBrowse() {
    fileInputRef.current.click();
  }

  function handleFileSelect(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = function() {
      setImage(reader.result);
    }
  }

  const handleSubmit = async(event) =>
   {
    event.preventDefault();
  
    const response = await axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/uploadimage/',
      data: {
        image : {image}
      }
    });

    if(response)
    {
      console.log('inside if')
      console.log(response.data.data)
    }else{
      console.log('nope')
    }
    // Clear the state
    setImage(null);
  }

  return (
    <div className="outer-Container">
      <div className="dropbox-container">
        {image ? (
          <img className="dropbox-image" src={image.toString()} alt="Dropped Image" />
        ) : (
          <div
            className="dropbox-area"
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onClick={handleBrowse}
          >
            <input type="file" accept="image/*" style={{display: 'none'}} ref={fileInputRef} onChange={handleFileSelect} />
            <p>Drop an image here or click to browse</p>
          </div>
        )}
      </div>
      { (
        <button className="dropbox-submit" onClick={handleSubmit}>
          Submit
        </button>
      )}
    </div>
  );
}

export default DropBox;
