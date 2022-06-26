import React, { useState } from 'react'
import TextField from '@material-ui/core/TextField';
import Autocomplete from '@material-ui/lab/Autocomplete';
import { Button } from '@material-ui/core';

var Searchbar  = () => {

const [myOptions, setMyOptions] = useState([])

const getDataFromAPI = () => {
	console.log("Options Fetched from API")

	fetch('http://dummy.restapiexample.com/api/v1/employees').then((response) => {
	return response.json()
	}).then((res) => {
	console.log(res.data)
	for (var i = 0; i < res.data.length; i++) {
		myOptions.push(res.data[i].employee_name)
	}
	setMyOptions(myOptions)
	})
}

return (
	<div style={{ marginLeft: '6%', marginTop: '3%' , height : '10px' , width : '85%' }}>
	<h3 style = {{marginLeft: '-3%' , width :'100%'}} > &nbsp; &nbsp;Add Another Keywords &nbsp; &nbsp; <button >1/3</button>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;</h3>
	<Autocomplete
		style={{ width: "99%" , height :10 }}
		freeSolo
		autoComplete
		autoHighlight
		options={myOptions}
		renderInput={(params) => (
		<TextField {...params}
			onChange={getDataFromAPI}
			variant="outlined"
			label="Search Box"
		/>
		)}
	/>
	</div>
);
}

export default Searchbar
