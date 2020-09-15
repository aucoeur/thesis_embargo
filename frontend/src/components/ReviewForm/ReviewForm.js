import React from 'react';

import './ReviewForm.scss';

function ReviewForm(props) {
    if (!props.data) {   
        return (
            <div>
                Updated props should show here when 'toggled' instead of using as link
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