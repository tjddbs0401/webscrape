import { BarChart, Bar, XAxis, YAxis, Tooltip } from "recharts";
import React from "react";

export default function Chart({ data }: any) {
  const byCategory = data.reduce((acc: any, b: any) => {
    acc[b.category] = (acc[b.category] || 0) + 1;
    return acc;
  }, {});
  const chartData = Object.entries(byCategory).map(([k, v]) => ({
    category: k,
    count: v,
  }));

  return (
    <BarChart width={400} height={200} data={chartData}>
      <XAxis dataKey="category" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="count" fill="#8884d8" />
    </BarChart>
  );
}
