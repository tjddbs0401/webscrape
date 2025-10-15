import React from "react";

export default function Filters({ value, onChange }: any) {
  return (
    <input
      className="border p-2 rounded mb-4 w-full"
      placeholder="Search title..."
      value={value}
      onChange={e => onChange(e.target.value)}
    />
  );
}
