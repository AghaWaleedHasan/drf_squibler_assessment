import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.css';
import SectionDataProvider from './components/DataProvider';
import SectionDisplay from './components/DataDisplay';

function App() {
  return (
    <div className="App">
      <header className='h1'>List All Sections</header>
      <SectionDataProvider endpoint='http://localhost:8000/' render={data => <SectionDisplay data={data}/>}/>
      {/* <h1>Hello World</h1> */}
    </div>
  );
}

export default App;
