//functional react component
import React from "react";
import "./productcard.css";

export default function ProductCard({ product }) {
  const sampleColors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD"];
  // Assign sample colors if product.colors is not provided
  if (!product.colors) {
    product.colors = sampleColors; // TODO: Replace with dynamic colors when available
  }
  // Assign a sample rating if product.rating is not provided
  if (!product.rating) {
    product.rating = 4.5; // TODO: Replace with dynamic rating when available
  }

  return (
    <div className="product-card">
      <img src={product.image} alt={product.name} className="product-image" />
      <section className="product-details">
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "space-between",
            marginBottom: "8px",
          }}
        >
          <div className="color-swatches">
            {product.colors.map((color, index) => (
              <span
                key={index}
                className="color-swatch"
                style={{
                  backgroundColor: color,
                }}
              ></span>
            ))}
          </div>
          <div className="product-rating">Rating: {product.rating} / 5</div>
        </div>
        <h3 className="product-name">{product.name}</h3>
        <p className="product-price">GHS {product.price.toFixed(2)}</p>
        <img
          src="/icons/plus-icon.svg"
          alt="Customize"
          className="customize-icon"
        />
      </section>
    </div>
  );
}
