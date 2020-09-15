import React, { useState } from 'react';

import ReviewForm from '../ReviewForm/ReviewForm';
import './GenerateForm.scss';

function GenerateForm() {
    const [data, setData ] = useState(null);

    return (
        <div>
            <div>
                <textarea rows="40"/>
            </div>
            <div>
                <input 
                    type="button" 
                    value="Generate"
                    onClick={ () => setData()} />
            </div>
            <ReviewForm data={ data ? data : null } />
        </div>
    )
}

export default GenerateForm;