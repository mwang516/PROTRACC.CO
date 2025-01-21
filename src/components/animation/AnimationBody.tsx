"use client"

import Link from "next/link";
import ThreeJSComponent from "./ThreeJSComponent";
import VideoComponent from "./VideoComponent";
import AnimationLoading from "./AnimationLoading";
import { useState } from 'react';

const AnimationBody = () => {
    const fileId = localStorage.getItem('file_id'); // Retrieve the fileId from local storage
    console.log('File ID:', fileId);
    const [isProcessing, setIsProcessing] = useState(true);

    return (
        <div className="flex flex-col items-center bg-amber-100 min-h-screen">
            <div className="h-12"></div>
          {/* 主内容容器 */}
          <div className="flex justify-center gap-8 p-8 w-full max-w-[2000px] mt-14 min-h-[80%]">
            {/* 左侧视频区域 */}
            <div className="flex-1 flex flex-col justify-center items-center border border-gray-8500 border-4 rounded-xl p-4 max-h-[600px] bg-black min-h-[80%]">
              <VideoComponent 
                fileId={fileId || ''} 
                setIsProcessing={setIsProcessing}
              />
              <p className="text-white">Video</p>
            </div>
            
            {/* 右侧动画或三维模型 */}
            <div className="flex-1 flex flex-col justify-center items-center border border-gray-8500 border-4 rounded-xl p-4 max-h-[600px] bg-black min-h-[80%]">
              {isProcessing ? <AnimationLoading /> : <ThreeJSComponent />}
              <p className="text-white">Animation: zoom in & out if animation is not on-screen</p>
            </div>
          </div>
          <Link href="/" className="bg-gray-900 text-white text-lg min-h-50 min-w-40 flex justify-center rounded-md shadow-md px-4, py-2 hover:underline">Finish & Return</Link>
        </div>
      );
      
}

export default AnimationBody;