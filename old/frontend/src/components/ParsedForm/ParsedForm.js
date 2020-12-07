import React from 'react';

import './ParsedForm.scss';

function ParsedForm(props) {
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

export default ParsedForm;