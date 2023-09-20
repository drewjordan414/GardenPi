import React from "react";
import { ChatEngine } from "react-chat-engine";
import ChatFeed from "./ChatFeed";

const Chat = () => {
    return (
        <ChatEngine
            height="100vh"  // This is the height of the chat window
            projectID="b0b0f0a2-0b0a-4b0b-8b0b-0b0b0b0b0b0b"
            userName="plant-health-dashboard"
            userSecret="plant-health-dashboard"
            renderChatFeed={(chatAppProps) => <ChatFeed {...chatAppProps} />}
        />
    )
};