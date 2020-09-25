import React from 'react';
import { NavLink } from 'react-router-dom';
import './Header.scss';

function Header() {
    return (
        <div className="Header">
            <header>
                <img src={`${process.env.PUBLIC_URL}/caltechlibrary-logo.png`} width="40%" height="40%" alt="caltechlibrary logo" />
                <h1>Thesis Embargo 6 Month Exception <br />Review Form Generator</h1>

                 <div>
                    <NavLink 
                        className="nav-link"   
                        activeClassName="nav-link-active" 
                        exact 
                        to="/">Form Builder</NavLink>  
                    </div>
            </header>
        </div>
    )
}

export default Header;