import React from 'react';

import './ReviewForm.scss';

function ReviewForm(props) {
    if (!props.data) {   
        return (
            <div>
                Parsed data will go here
            </div>
        )
    } else {
        return (
            <div className='processed'>
                {props.data}
            </div>
        )
    }
}

export default ReviewForm;