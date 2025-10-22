import React, { useEffect, useRef, useState } from "react";
import * as fabric from "fabric";

const Designer = ({ image = "/samples/black-t-front.png" }) => {
  const canvasRef = useRef(null);

  const fabricCanvasRef = useRef(null);

  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    if (canvasRef.current && !fabricCanvasRef.current) {
      const canvas = new fabric.Canvas(canvasRef.current, {
        height: 400,
        width: 600,
        backgroundColor: "#f8f8f8",
      });

      fabricCanvasRef.current = canvas;
      setIsReady(true);

      fabric.FabricImage.fromURL(image, function (oImg) {
        oImg.height = 300;
        oImg.width = 200;
        // canvas.add(oImg);
      });
    }

    return () => {
      if (fabricCanvasRef.current) {
        fabricCanvasRef.current.dispose();
        fabricCanvasRef.current = null;
      }
    };
  }, []);

  // useEffect(() => {
  //   if (isReady) {
  //     console.log('Fabric canvas is ready and accessible via fabricCanvasRef.current');
  //   }
  // }, [isReady]);

  return (
    <div>
      <h2>Make your own customization</h2>
      <canvas ref={canvasRef} />
      {!isReady && <p>Loading canvas...</p>}
    </div>
  );
};

export default Designer;
