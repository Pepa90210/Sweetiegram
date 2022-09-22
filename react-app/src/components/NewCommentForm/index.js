import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { createCommentThunk } from "../../store/comments";
import "./NewCommentForm.css"

const CommentForm = ({ postId }) => {
  const dispatch = useDispatch();

  const [content, setContent] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    const contentObj = { "content": content }
    dispatch(createCommentThunk(postId, contentObj));
  };

  return (
   
      
        <form id="create-new-comment-form" onSubmit={handleSubmit}>
          <label>
            <input
              id="content-area-input"
              type="textarea"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              required
              placeholder="Add a comment..."
            />
          </label>
          <button id="comment-submit-button" type="submit">
            Post
          </button>
        </form>
  );
};

export default CommentForm;
