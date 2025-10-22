import React from "react";
import "./ProductGrid.css";
import ProductCard from "../ProductCard/ProductCard";

export default function ProductGrid({
  products = [
    { name: "T-shirt", image: "/samples/apparel.jpg", price: 25 },
    { name: "Apron", image: "/samples/apron.jpg", price: 25 },
    { name: "Bags", image: "/samples/bags.jpeg", price: 25 },
    { name: "Bottles", image: "/samples/bottles.jpg", price: 25 },
    { name: "Jacket", image: "/samples/jacket.jpg", price: 25 },
  ],
}) {
  return (
    <div className="product-grid-container">
      <div className="product-grid">
        {products.map((product, idx) => (
          <ProductCard key={idx} product={product} />
        ))}
      </div>
    </div>
  );
}
