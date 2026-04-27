 import { describe, expect, it } from 'vitest'
 import {fireEvent, getByTestId, render, screen} from '@testing-library/react';
 import userEvent from '@testing-library/user-event'
 import '@testing-library/jest-dom/vitest';
 import App from './App';
 describe("App Component Tests", ()=> {
    it('App renders', () => {
        render(<App />);
        let element = screen.getByText(/App/i);
        expect(element).toBeInTheDocument()
    })

    it('increments the count when clicked', async () => {
        render(<App />)

        const button = screen.getByRole('button', { name: /count is/i })
        expect(button).toHaveTextContent('Count is 0')

        const user = userEvent.setup()
        await user.click(button)

        expect(button).toHaveTextContent('Count is 1')
    })

    it('increments the counter again', async() => {
        render(<App />)

        // Not recommended
        const button = screen.getByText(/count is/i)

        fireEvent.click( button )
        fireEvent.click( button )
        expect(button).toHaveTextContent(/Count is 2/)
    })
 })