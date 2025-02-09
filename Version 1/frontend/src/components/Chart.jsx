import * as React from 'react';
import { BarChart } from '@mui/x-charts/BarChart';

export default function Chart(props){
    return (
        <BarChart
        xAxis={[{ scaleType: 'band', data: ['Total Yearly Cost', 'Total Yearly Savings'] }]}
        series={[
            { data: [props.a, props.b] }
        ]}
        width={500}
        height={300}
        />
    );
}