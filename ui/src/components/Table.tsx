import React from "react";

export default function Table({ data }: any) {
  return (
    <table className="border w-full text-left">
      <thead>
        <tr>
          <th>Title</th><th>Price</th><th>Rating</th><th>Category</th>
        </tr>
      </thead>
      <tbody>
        {data.map((b: any, i: number) => (
          <tr key={i}>
            <td>{b.title}</td>
            <td>{b.price}</td>
            <td>{b.rating}</td>
            <td>{b.category}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
