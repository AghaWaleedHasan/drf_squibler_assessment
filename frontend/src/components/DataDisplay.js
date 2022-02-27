import React, { Component } from 'react';

class Recursive extends Component {
    state = {  } 
    render() { 
        let childitems = null;

        if (this.props.children) {
            childitems = this.props.children.map(child => (
                <Recursive item={child} children={child.children}/>
            ))
        }
        return (
            <li key={this.props.item.id}>
                {this.props.item.title}
                <p>{this.props.item.content}</p>
                { childitems ? <ul>{childitems}</ul> : null}
            </li>
        );
    }
}

class SectionDisplay extends Component {
    state = {  } 
    render() { 
        let items = this.props.data.map((item) => (
            <Recursive item={item} children={item.children}/>
        ))
        return (
            <ul>
                {items}
            </ul>
        );
    }
}
 
export default SectionDisplay;