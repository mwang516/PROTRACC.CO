"use client"

import React, { useState, useEffect } from 'react';

// Example in a React component
const ThreeJSComponent: React.FC = () => {
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const handleThreeJSReady = (event: MessageEvent) => {
            if (event.data === 'threejs-ready') {
                setIsLoading(false);
            }
        };

        window.addEventListener('message', handleThreeJSReady);

        // Cleanup listener and timeout
        return () => {
            window.removeEventListener('message', handleThreeJSReady);
        };
    }, []);

    return (
        <>
            {isLoading && (
                <div className="absolute inset-0 flex items-center justify-center bg-white">
                    <div className="text-center">
                        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-gray-900"></div>
                        <p className="mt-4">Loading 3D visualization...</p>
                    </div>
                </div>
            )}
            <iframe
                src="/threejs.html"
                style={{ 
                    width: '100%', 
                    height: '100%', 
                    border: 'none',
                    visibility: isLoading ? 'hidden' : 'visible' 
                }}
                title="Three.js Scene"
            />
        </>
    );
};

export default ThreeJSComponent;