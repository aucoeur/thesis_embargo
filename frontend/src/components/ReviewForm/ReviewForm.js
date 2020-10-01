import React from 'react';
import { useForm } from 'react-hook-form';
import SignaturePad from 'react-signature-pad-wrapper'

import './ReviewForm.scss';

function ReviewForm() {
  const { register, handleSubmit, errors } = useForm();
  const onSubmit = data => console.log(data);
  console.log(errors);
  
  return (
    <div className="col">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className="col">
          <label>Comments</label>
          <textarea name="Comments" ref={register} />
        </div>
        <div className="row">
          
        <input name="Thesis Embargo Decision" type="radio" value="Approve" ref={register({ required: true })}/> Approve
        <input name="Thesis Embargo Decision" type="radio" value="Deny" ref={register({ required: true })}/> Deny
        </div>
        <div className="col">
          <div className="sig">
            <SignaturePad redrawOnResize={true} options={{minWidth: 1, maxWidth: 2, penColor: 'rgb(0, 0, 200)', backgroundColor: 'rgb(255, 255, 255)'}} />
          </div>
          <input type="button" value="Submit"/>
        </div>

      </form>
    </div>
  );
}

export default ReviewForm;