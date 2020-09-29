import React, { useState } from 'react';
import reactStringReplace from "react-string-replace";
import ReviewForm from '../ReviewForm/ReviewForm';
import './GenerateForm.scss';

const strReplace = reactStringReplace;

let testString = "Submitted values are:Reason for Requesting Exception: Chapters 2 and 3 are submitted for publication in ACS Catalysis.Requestor Name: Melissa RayRequestor Email: melray@library.caltech.eduThesis Author: Melissa RayThesis Title: SAMPLE - C(sp³)–H Activation via Dehydrogenation of Cyclic and Heterocyclic Alkanes by Single-Site IridiumPincer Ligated CompleGraduation Year: 2020Advisor Name: Robert Grubbs, Brian StoltzAdvisor Email: rhg@caltech.edu,stoltz@caltech.eduDivision: Chemistry and Chemical Engineering (CCE)Exception Type: Extend Embargo to Caltech Campus (i.e., prohibit access from campus)Request: Consistent with the Caltech Doctoral Thesis Dissemination policy, I am requesting an exception to the 6-monthembargo to campus for my PhD thesis."

//(?<=<\/div>)(([\w\d\s]+[@()\.-]?\.?)|([\w-]+@([\w-]+\.)+[\w-]+?)(\,?))(?=<div>)

// (?<=<\/div>)(.*?)(?=<div>|<\/div>)

function GenerateForm() {
    const [ data, setData ] = useState("");
    const [ processedData, setProcessedData ] = useState("");

    function transformData(newData) {
        const headers = ["Reason for Requesting Exception: ", "Requestor Name: ", "Requestor Email: ", "Thesis Author: ", "Thesis Title: ", "Graduation Year: ", "Advisor Name: ", "Advisor Email: ", "Division: ", "Exception Type: ", "Request: " ]
        
        let replacedText = newData;
        
        // wraps headers in div and span
        for (let i =0; i < headers.length; i++) {            
            replacedText = strReplace(replacedText, headers[i], () => (
                <span className="header">{headers[i]}</span>
                )
            );
        // wraps remaining text in a span
        }
        replacedText = strReplace(replacedText, /(.*)/g, (match, i) => (
            <span key={Math.random()+match} className="entry">{match}<br /></span>
            )
        );
        console.log(replacedText)

        return replacedText;
    }

    return (
        <div className="container">
            <div>
                <textarea 
                    rows="10"
                    value={data}
                    onChange= {(e) => setData(e.target.value)}
                    />
            </div>
            <div>
                <input 
                    type="button" 
                    value="Generate"
                    onClick={ () => setProcessedData(transformData(data)) } />
            </div>
            <div className="container">
                <h1>Parsed Form Data</h1>
                <div className="parsed">
                    <ReviewForm data={ processedData ? processedData : null } />
                </div>
            </div>
        </div>
    )
}

export default GenerateForm;