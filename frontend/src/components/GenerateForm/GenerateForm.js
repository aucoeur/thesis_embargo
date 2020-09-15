import React, { useState } from 'react';

import ReviewForm from '../ReviewForm/ReviewForm';
import './GenerateForm.scss';

function GenerateForm() {
    const [ data, setData ] = useState("");
    const [ processedData, setProcessedData ] = useState("");

    function transformData(data) {
        return data.toUpperCase();
    }


    return (
        <div>
            <div>
                <textarea 
                    rows="40"
                    value={data}
                    onChange= {(e) => setData(e.target.value)}
                    />
            </div>
            <div>
                <input 
                    type="button" 
                    value="Generate"
                    onClick={ () => setProcessedData( entry => [...entry, transformData(data)])} />
            </div>
            <div>
                <h1>Generated Form</h1>
                <ReviewForm data={ processedData ? processedData : null } />
            </div>
        </div>
    )
}

export default GenerateForm;