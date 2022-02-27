import React, { Component } from 'react';

class SectionDataProvider extends Component {
    state = { 
        data: []
     } 

    componentDidMount() {
        fetch(this.props.endpoint).then(
            response => response.json()
        ).then(
            data => this.setState({ data })
        )
    };

    render() { 
        return (
            this.props.render(this.state.data)
        );
    }
}
 
export default SectionDataProvider;