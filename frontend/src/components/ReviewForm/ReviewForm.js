import React, { useRef, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import SignaturePad from 'react-signature-pad-wrapper'

import './ReviewForm.scss';

function ReviewForm() {
    const { register, handleSubmit, errors } = useForm();
    const onSubmit = data => console.log(data);
    console.log(errors);

    const signbox = useRef();
    const clear = () => {
        signbox.current.clear()
    }
    // useEffect( () => {signbox.current.clear() }) 

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
                <div className='sig'>
                <SignaturePad className="sig" clearButton={true} redrawOnResize={true} options={{penColor: 'rgb(0, 0, 200)', backgroundColor: 'rgb(255, 255, 255)'}} />
                </div>
            <div className="row">
                <input type="button" value="Submit"/><input type="button" value="Clear" onClick={clear}/>
                </div>
            </div>

        </form>
        </div>
    );
}

export default ReviewForm;